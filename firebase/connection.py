import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 用自己存放的路徑
cred = credentials.Certificate('D:\\work_space\\python\\boris_bot\\firebase\\serviceAccount.json')
firebase_admin.initialize_app(cred)
