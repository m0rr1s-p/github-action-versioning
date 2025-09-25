from versioning import increment_version

def test_increment_version():
    assert increment_version("1.0.0", "major", 99) == "2.0.0"
    assert increment_version("1.2.99", "minor", 99) == "1.3.0"
    assert increment_version("1.2.99", "patch", 99) == "1.3.0"
    assert increment_version("1.99.99", "minor", 99) == "2.0.0"
    assert increment_version("1.99.99", "patch", 99) == "2.0.0"
    assert increment_version("1.23.32", "patch", 99) == "1.23.33"