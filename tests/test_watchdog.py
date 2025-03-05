import pytest
from unittest.mock import MagicMock, patch
from watchdog.events import FileSystemEvent
from src.sync.watchdog import SyncHandler, start_monitoring

@pytest.fixture
def mock_logger():
    return MagicMock()

@pytest.fixture
def mock_sync_folders():
    with patch("src.sync.sync_logic.sync_folders") as mock:
        yield mock

@pytest.fixture
def mock_observer():
    with patch("watchdog.observers.Observer") as mock:
        yield mock

def test_sync_handler_on_any_event(mock_logger, mock_sync_folders):
    source = "source_path"
    replica = "replica_path"
    event_handler = SyncHandler(source, replica, mock_logger)
    event = MagicMock(spec=FileSystemEvent)

    event_handler.on_any_event(event)
    mock_sync_folders.assert_called_once_with(source, replica, mock_logger)

def test_start_monitoring(mock_logger, mock_observer):
    source = "source_path"
    replica = "replica_path"
    log_file = "log.txt"

    with patch("src.sync.logger.Logger", return_value=mock_logger):
        with patch("time.sleep", side_effect=KeyboardInterrupt):
            start_monitoring(source, replica, log_file)

    mock_observer.assert_called_once()
