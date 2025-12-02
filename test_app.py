import pytest
from app import app  # Make sure this matches your filename
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

@pytest.fixture
def dash_app():
    return app

def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header.text == "SoulFood"

def test_visualisation_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales\\ by\\ date\\ data")
    assert graph is not None

def test_region_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio = dash_duo.find_element("#region-selector")
    assert radio is not None