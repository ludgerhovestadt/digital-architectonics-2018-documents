import bpy, bmesh

verts = [(0, 0, 0), (0, 5, 0), (5, 5, 0), (5, 0, 0)]
edges = [()]
faces = [(0,1, 2, 3)]

mesh = bpy.data.meshes.new("mesh")  # add a new mesh
mesh.from_pydata(verts, edges, faces) # define vertices and faces
obj = bpy.data.objects.new("MyObject", mesh)  # add a new object using the mesh

scene = bpy.context.scene # get the scene
scene.objects.link(obj)  # put the object into the scene (link)
scene.objects.active = obj  # set as the active object in the scene
obj.select = True  # select object
