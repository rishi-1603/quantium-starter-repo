from app import app

def test_app_exists():
    assert app is not None

def test_layout_exists():
    assert app.layout is not None


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header")


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#visualization")


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-picker")