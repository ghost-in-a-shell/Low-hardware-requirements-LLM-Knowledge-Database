from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.vectorstores import Chroma

print("loading source files...\t") 
loader = PyPDFLoader("./srcfiles/test.pdf")
pages = loader.load_and_split()
print("done!\n") 

print("splitting documents...\t") 
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=0,
    separators=["\n\n", "\n", "(?<=\. )","(?<=。)", " ", ""]
)
splits = r_splitter.split_documents(pages)
print (len(splits))
print("done!\n") 

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('../intfloat_multilingual-e5-base')
input_texts = [
    'query: how much protein should a female eat',
    'query: 南瓜的家常做法',
    "passage: As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 i     s 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or traini     ng for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "passage: 1.清炒南瓜丝 原料:嫩南瓜半个 调料:葱、盐、白糖、鸡精 做法: 1、南瓜用刀薄薄的削去表面一层皮     ,用勺子刮去瓤 2、擦成细丝(没有擦菜板就用刀慢慢切成细丝) 3、锅烧热放油,入葱花煸出香味 4、入南瓜丝快速翻炒一分钟左右,     放盐、一点白糖和鸡精调味出锅 2.香葱炒南瓜 原料:南瓜1只 调料:香葱、蒜末、橄榄油、盐 做法: 1、将南瓜去皮,切成片 2、油     锅8成热后,将蒜末放入爆香 3、爆香后,将南瓜片放入,翻炒 4、在翻炒的同时,可以不时地往锅里加水,但不要太多 5、放入盐,炒匀      6、南瓜差不多软和绵了之后,就可以关火 7、撒入香葱,即可出锅"
]
embeddings = model.encode(input_texts, normalize_embeddings=True)
print(embeddings)