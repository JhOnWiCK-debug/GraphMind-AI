class SourceTracker:

    def __init__(self):

        self.graph_sources = []

        self.document_sources = []

    def add_graph_source(
        self,
        source
    ):

        self.graph_sources.append(
            source
        )

    def add_document_source(
        self,
        source
    ):

        self.document_sources.append(
            source
        )

    def get_sources(self):

        return {

            "graph": self.graph_sources,

            "documents": self.document_sources
        }

    def clear(self):

        self.graph_sources.clear()

        self.document_sources.clear()