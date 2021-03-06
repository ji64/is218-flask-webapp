"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link active" href="/page1">Git</a>' in response.data
    assert b'<a class="nav-link active" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link active" href="/page3">Python</a>' in response.data
    assert b'<a class="nav-link active" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link active" href="/page5">OOP Glossary</a>' in response.data
    assert b'<a class="nav-link active" href="/page6">AAA</a>' in response.data
    assert b'<a class="nav-link active" href="/page7">Principles</a>' in response.data
    assert b'<a class="nav-link active" href="/page8">SOLID</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Proxmox" in response.data

def test_request_page1(client):
    """This checks page 1"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This checks page 2"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This checks page 3"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python / Flask" in response.data

def test_request_page4(client):
    """This checks page 4"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Continuous Integration and Deployment" in response.data

def test_request_page5(client):
    """This checks page 5"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"OOP Glossary" in response.data

def test_request_page6(client):
    """This checks page 6"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"Arrange-Act-Assert Testing" in response.data

def test_request_page7(client):
    """This checks page 7"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"OOPs" in response.data

def test_request_page8(client):
    """This checks page 8"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page10")
    assert response.status_code == 404

