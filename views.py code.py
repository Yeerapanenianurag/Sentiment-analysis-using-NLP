from django.http import HttpResponse
from django.shortcuts import render
from io import TextIOWrapper
import csv
from collections import defaultdict

# Create your views here.
from admins.models import storedatamodel
from django_pandas.io import read_frame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

def index(request):
    return render(request, 'index.html')

def adminlogin(request):
    return render(request, "admins/adminlogin.html")

def logout(request):
    return render(request, 'index.html')

def adminloginentered(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['upasswd']
        if uname == 'admin' and passwd == 'admin@2020':
            return render(request, "admins/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")

def storecsvdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        csvfile = TextIOWrapper(request.FILES['file'], encoding='utf-8')
        columns = defaultdict(list)
        storecsvdata = csv.DictReader(csvfile)
        for row1 in storecsvdata:
            #id = row1["id"]
            label = row1["label"]
            tweet = row1["tweet"]
            storedatamodel.objects.create(label=label, tweet=tweet)
        print("Name is ", csvfile)
        return HttpResponse('CSV file successful uploaded')
    else:
        return render(request, 'admins/storedata.html', {})

def NaiveBayes(request):
    qs = storedatamodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    # data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    #print(data.shape)
    # print("data-label:",data.label)
    dataset = data.iloc[:, [0, 1]].values
    print("x", dataset)
    dataset1 = data.iloc[:, 1].values
    print("y", dataset1)
    print("shape", dataset.shape)
    X = dataset
    y = dataset1
    print(dataset.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)
    st_X = StandardScaler()
    X_train = st_X.fit_transform(X_train)
    X_test = st_X.transform(X_test)
    classifier = KNeighborsClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print("y_pred", y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print("cm", cm)
    accurancy = classifier.score(X_train, y_train)
    print("accurancy", accurancy)
    predicition = classification_report(y_test, y_pred)
    print("predicition", predicition)
    x = predicition.split()
    print("Toctal splits ", len(x))
    dict = {
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
    }
    return render(request, 'admins/NaiveBayes.html', dict)

def svm(request):
    qs = storedatamodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    data.info()
    print(data.head())
    print(data.describe())
    # print("data-label:",data.label)
    dataset = data.iloc[:, [0, 1]].values
    print("x", dataset)
    dataset1 = data.iloc[:, 1].values
    print("y", dataset1)
    print("shape", dataset.shape)
    X = dataset
    y = dataset1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    # print(svclassifier.predict([0.58, 0.76]))
    y_pred = svclassifier.predict(X_test)
    m = confusion_matrix(y_test, y_pred)
    accurancy = classification_report(y_test, y_pred)
    print(m)
    print(accurancy)
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {
        #"m": m,
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
    }
    return render(request, 'admins/svm.html', dict)