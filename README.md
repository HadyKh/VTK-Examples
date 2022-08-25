# VTK

VTk tutorials Official website: https://kitware.github.io/vtk-examples/site/Python/

VTK has two models: 

visualization model &emsp; &&& &emsp; Graphics model

Source &#8594; Filter &#8594; Mapper &#8594; Actor &#8594; Renderer

<ins>Source:</ins> External data source or generate data<br>
<ins>Filter:</ins> transform data input 'Transformation' produce geometry or visualization objects but they are note graphics objects yet<br>
<ins>Mapper:</ins> process convert filter outputs to anobject that can be displayed (graphics model object) to be sent to the graphics model 'Actor & renderer'<br>


# VTK steps
{
    
    create Geometry;
    create a mapper;
    give the geometry to the mapper

    create an actor;
    give the mapper to the actor;

    create renderer;
    give the actor to the renderer;

    create a randerer window;
    give the renderer to the window;

    create window interactor;
    give the renderer window to the window interactor;

    start the window interactor;
}

<ins>you may need to add camera or light</ins>
renderer.GetActiveCamera().SetPosition(9.0, 9.0, 7.0)<br>
renderer.GetActiveCamera().SetFocalPoint(0, 0, 0)<br>
renderer.GetActiveCamera().SetViewUp(0.2, -0.7, 0.7)<br>
renderer.GetActiveCamera().SetDistance(14.5)<br>

