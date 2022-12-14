import vtk

#-------Data source--------
cube = vtk.vtkCubeSource()

#-----------mapper---------------
cubeMapper = vtk.vtkPolyDataMapper()
# setInput & GetOutPut: used to connect different objects
# So, it will get the cube output to be used as input to the mapper
cubeMapper.SetInputConnection(cube.GetOutputPort())

#---------------actor---------------
cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetColor(1, 0, 0)

#---------------rendering window & renderer---------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(cubeActor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer)
renderWindow.Render()

#---------------render Window Interactor---------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()