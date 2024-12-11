import cmf

# for help https://philippkraft.github.io/cmf/classcmf_1_1project.html

p = cmf.project()

cell = p.NewCell(0,0,0,1000) # (double x, double y, double z, double area, bool with_surfacewater=false)

W1 = p.NewStorage()

