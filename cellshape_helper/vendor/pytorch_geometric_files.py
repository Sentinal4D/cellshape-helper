"""
Functions adapted from PyTorch Geometric
"""
import torch


def parse_txt_array(src, sep=None, start=0, end=None, dtype=None):
    src = [[float(x) for x in line.split(sep)[start:end]] for line in src]
    src = torch.tensor(src, dtype=dtype).squeeze()
    return src


def parse_off(src):
    # Some files may contain a bug and do not have a carriage return after OFF.
    if src[0] == "OFF":
        src = src[1:]
    else:
        src[0] = src[0][3:]

    num_nodes, num_faces = [int(float(item)) for item in src[0].split()[:2]]

    pos = parse_txt_array(src[1 : 1 + num_nodes])
    face = src[1 + num_nodes : 1 + num_nodes + num_faces]
    face = face_to_tri(face)
    data = {"pos": pos, "face": face}

    return data


def face_to_tri(face):
    face = [[int(x) for x in line.strip().split()] for line in face]

    triangle = torch.tensor([line[1:] for line in face if line[0] == 3])
    triangle = triangle.to(torch.int64)

    rect = torch.tensor([line[1:] for line in face if line[0] == 4])
    rect = rect.to(torch.int64)

    if rect.numel() > 0:
        first, second = rect[:, [0, 1, 2]], rect[:, [0, 2, 3]]
        return torch.cat([triangle, first, second], dim=0).t().contiguous()
    else:
        return triangle.t().contiguous()


def read_off(path):
    r"""Reads an OFF (Object File Format) file, returning both the position of
    nodes and their connectivity in a :class:`torch_geometric.data.Data`
    object.
    Args:
        path (str): The path to the file.
    """
    with open(path, "r") as f:
        src = f.read().split("\n")[:-1]
    return parse_off(src)


def sample_points(data, num):
    pos, face = data["pos"], data["face"]
    assert pos.size(1) == 3 and face.size(0) == 3

    pos_max = pos.abs().max()
    pos = pos / pos_max

    area = (pos[face[1]] - pos[face[0]]).cross(pos[face[2]] - pos[face[0]])
    area = area.norm(p=2, dim=1).abs() / 2

    prob = area / area.sum()
    sample = torch.multinomial(prob, num, replacement=True)
    face = face[:, sample]

    frac = torch.rand(num, 2)
    mask = frac.sum(dim=-1) > 1
    frac[mask] = 1 - frac[mask]

    vec1 = pos[face[1]] - pos[face[0]]
    vec2 = pos[face[2]] - pos[face[0]]

    pos_sampled = pos[face[0]]
    pos_sampled += frac[:, :1] * vec1
    pos_sampled += frac[:, 1:] * vec2

    pos_sampled = pos_sampled * pos_max

    return pos_sampled
