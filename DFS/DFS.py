def  dfs(node, goal, tmap, duyetRoi, path):
  if (node == goal):
    print("\n Da tim thay Goal ", goal)
    print(" Path = ", path)
    return True
  elif not (node in duyetRoi):
    print("\n Node", node)
    duyetRoi.append(node)
    path.append(node)
    conNode = []
    if (node in tmap.keys()):
      conNode = tmap[node].keys()
    print("\n\t Node ", node, " co con ", conNode)

    for tungcon in conNode:
      x = dfs(tungcon, goal, tmap, duyetRoi, path)
      if (x):
        return x
    return False
  else:
    print("\n\t ... da duyet ", node)
    return False
