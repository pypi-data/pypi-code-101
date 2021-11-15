from unittest.mock import Mock
import tarfile, os
import pytest
from gladier_tools.posix.untar import untar_file

@pytest.fixture
def mock_isfile(monkeypatch):
    """Mock isfile. Returns False by default"""
    monkeypatch.setattr(os.path, 'isfile', Mock(return_value=False))
    return os.path.isfile

def test_no_file(monkeypatch, mock_isfile):
    with pytest.raises(NameError):
        untar_file()

def test_mkdir(monkeypatch, mock_isfile, mock_tar):
    mock_isfile.return_value= True
    monkeypatch.setattr(os.path, 'exists', Mock(return_value=False))
    mock_mkdir= Mock()
    monkeypatch.setattr(os, 'makedirs', mock_mkdir)
    mock_tf, mock_context_manager= mock_tar
    untar_file()
    assert mock_mkdir.called
    assert mock_tf.called
    assert mock_context_manager.extractall.called
    


