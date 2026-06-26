from source_tracker import (
    SourceTracker
)

tracker = SourceTracker()

tracker.add_graph_source(
    "Wheelz --imports_from--> China"
)

tracker.add_graph_source(
    "China --currency--> Yuan"
)

tracker.add_document_source(
    "Chunk 12"
)

tracker.add_document_source(
    "Chunk 18"
)

print()

print(
    tracker.get_sources()
)