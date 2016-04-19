import numpy as np


def get_center_of_patch(graph, out=None):
    from .ext.remap_element import calc_center_of_patch

    n_patches = graph.number_of_patches

    if out is None:
        out = np.empty((n_patches, 2), dtype=float)

    calc_center_of_patch(links_at_patch, offset_to_patch,
                         xy_of_link, out)

    return out


def get_area_of_patch(graph, out=None):
    from .ext.of_patch import calc_area_of_patch

    if out is None:
        out = np.empty(n_patches, dtype=float)

    calc_area_of_patch(graph.nodes_at_patch, out)

    return out