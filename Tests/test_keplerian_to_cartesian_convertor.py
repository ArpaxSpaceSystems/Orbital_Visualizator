from src.orbital_visualizator.keplerian_to_cartesian_convertor import orbit_calculation
import pytest

def test_calcul_orbit():
    
    x, y, z = orbit_calculation(orbital_parameters=[36000,0.00025,0.45,0.48,0.58,1.25,"Test_Probe"],theta=1.25)
    
    assert x == pytest.approx(-22312.2, rel=0.1)    #fucntion Orbit_Calculation contains trigonometric function hence approximation for assert tests
    assert y == pytest.approx(23642.43, rel=0.1)
    assert z == pytest.approx(15459.52, rel=0.1)

