import matplotlib.pyplot as plt
import base64
from io import BytesIO

# 가능한 font list 확인
import matplotlib.font_manager as fm
# f = [f.name for f in fm.fontManager.ttflist]
# print(f)

# 확인 이후
plt.rc('font', family='Malgun Gothic')

def get_graph():
    buffer= BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph =  base64.b64encode(image_png)
    graph = graph.decode('UTF-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("product")
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Catagory')
    plt.ylabel('Number')
    plt.tight_layout()
    graph =  get_graph()
    return graph
