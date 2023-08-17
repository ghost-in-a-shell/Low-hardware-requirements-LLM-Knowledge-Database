#paths
CHROMADB_PATH="../chroma_vectordb/"
FILEARRAY_PATH="../arrays/"
SRCFILE_PATH="./srcfiles/"
EMBEDDING_PATH="../intfloat_multilingual-e5-base"
COOKIE_PATH="./"

#split params
SPLITRCTS_CHUNKSIZE=150
SPLITRCTS_OVERLAP=0
SPLITRCTS_SEPARATORS=["\n\n", "\n", "(?<=\. )","(?<=。)", " ", ""]

#llm params
NEAREST_K=5
HALF_SEARCH_RANGE=3

#debug
DEBUG=False

#input
INUPT_TYPES=['pdf','docx','pptx','txt','md','png']

#poe
QUORA_FORMKEY='xxx'
QUORA_COOKIES='m-b=xxx'
POE_BOT='chinchilla'