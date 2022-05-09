"""Tests for `pca.packages.package_example` package."""


def test_pca_namespace():
    """Test the package is accessible through the `pca` namespace"""
    from pca.packages import package_example

    assert hasattr(package_example, "VERSION")
