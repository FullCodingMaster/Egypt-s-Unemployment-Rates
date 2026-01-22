import API.api as api
import analyzer.analyzer as analyzer
import Visualization.visual as visual

if __name__ == "__main__":
    data = analyzer.get_data()
    visual.show_data(data=data)
