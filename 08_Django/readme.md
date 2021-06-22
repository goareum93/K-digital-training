# Django

2021.06.23 일 수업내용 기준으로 작성한 것입니다.



## 설치하기

anaconda Powershell에서 다음과 같이 작성

```powershell
  conda deactivate

  conda create --name django python=3.8.3

  conda env list

  conda activate django

  pip install ipykernel

  python -m ipykernel install --user --name django --display-name "Python Django"

  conda install -c conda-forge jupyterlab
  
  # Django installation
    pip install Django==3.2.4
    
python -m django --version

cd Desktop

cd 2021-K-Digital-Training-main
# 바탕화면에 저 폴더가 있어야 이게 실행돼요! 확인!!

django-admin startproject mysite

dir
#mysite 있는지 확인

cd mysite

python manage.py
```



vs code를 열어서 mysite 폴더를 오픈한다.

![image-20210623002628730](readme.assets/image-20210623002628730.png)

vs code에서 +밑에 v 아래 화살표 표시를 눌러  command prompt 저거 누른다

![image-20210623002706809](readme.assets/image-20210623002706809.png)

```
conda activate django
```

위의 코드를 실행시키면 아래와 같이 (django)로 활성화 된것을 확인할 수 있다.

![image-20210623002822403](readme.assets/image-20210623002822403.png)





단, 아래의 오류가 났을 경우 anaconda의 경로 설정 문제가 있었을지도 모른다. 

```
C:\Users\admin\Desktop\2021-K-Digital-Training-main\mysite>conda activate django
'conda'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.
```

그렇다면 아래와 같이 환경변수에 Anaconda 경로를 넣어줘야한다. 

- 시작버튼 누르고 시스템 환경변수 편집을 검색하고 고급에서 환경변수를 클릭

- Path를 누르고 편집 클릭

- 그리고 아래 그림에 나타나 있는 Anaconda 관련 코드를 작성하면 된다. 단, 개인별로 admin 이라고 쓴 폴더명이 다를수 있으니 체크하기!

![image-20210623003340253](readme.assets/image-20210623003340253.png)

- 다시 vs code로 돌아가서 command prompt 에 `conda activate django`를 실행시켜보면 (django)로 활성화 된것을 확인할 수 있다.



## 장고 앱 작성

### 프로젝트 만들기

django 홈페이지에 나타난 앱 작성하기 예시를 따라할 것이다.

https://docs.djangoproject.com/ko/3.2/intro/tutorial01/

이 튜토리얼을 통해, 간단한 설문조사(Polls) 어플리케이션을 만드는 과정을 따라해 보자.

다음 명령을 실행하여 Django가 설치되어 있고 어떤 버전인지 알 수 있다.

```shell
$ python -m django --version
```

 `cd` 명령으로 코드를 저장할 디렉토리로 이동 한 후, 다음의 명령을 수행한다.

```shell
$ django-admin startproject mysite
```

이 명령은 현재 디렉토리에서 `mysite`라는 디렉토리를 생성할 것이다.

### 개발 서버

당신의 Django 프로젝트가 제대로 동작하는지 확인해보자. `mysite` 디렉토리로 이동하고, 다음 명령어를 입력

```shell
$ python manage.py runserver
```

이제 서버가 동작하기 시작했으니, 자신의 웹 브라우져에서 http://127.0.0.1:8000/ 을 통해 접속할 수 있다. 로켓이 이륙하는 모습이 담긴 《Congratulations!》 페이지를 보게된다.

![image-20210623004643366](readme.assets/image-20210623004643366.png)



앱을 생성하기 위해 `manage.py`가 존재하는 디렉토리에서 다음의 명령을 입력해 보자.

```shell
$ python manage.py startapp polls
```

dir를 통해 안에 어떤파일들이 생겼는지 파악해보자.



### 첫 번째 뷰 작성하기

첫 번째 뷰를 작성해보자. 《polls/view.py》를 열어 다음과 같은 파이썬 코드를 입력

```shell
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Django에서 가장 간단한 형태의 뷰이다. 뷰를 호출하려면 이와 연결된 URL 이 있어야 하는데, 이를 위해 URLconf가 사용됨

polls 디렉토리에서 URLconf를 생성하려면, `urls.py`라는 파일을 생성해야 합니다. 



《polls/urls.py》 파일에는 다음과 같은 코드가 포함되어 있습니다.

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

다음 단계는, 최상위 URLconf 에서 `polls.urls` 모듈을 바라보게 설정합니다. 

`mysite/urls.py` 파일을 열고, `django.urls.include`를 import 하고, `urlpatterns` 리스트에 [`include()`](https://docs.djangoproject.com/ko/3.2/ref/urls/#django.urls.include) 함수를 다음과 같이 추가합니다.

```shell
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```



### 데이터베이스 설치

참고 : https://docs.djangoproject.com/ko/3.2/intro/tutorial02/

이제, `mysite/settings.py` 파일을 열어보세요. 이 파일은 Django 설정을 모듈 변수로 표현한 보통의 Python 모듈입니다.

다른 데이터베이스를 사용해보고 싶다면, 적절한 [데이터베이스 바인딩](https://docs.djangoproject.com/ko/3.2/topics/install/#database-installation)을 설치하고, 데이터베이스 연결 설정과 맞게끔 [`DATABASES`](https://docs.djangoproject.com/ko/3.2/ref/settings/#std:setting-DATABASES) `'default'` 항목의 값을 다음의 키 값으로 바꿔주세요.

- [`ENGINE`](https://docs.djangoproject.com/ko/3.2/ref/settings/#std:setting-DATABASE-ENGINE) – `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'`, 또는 `'django.db.backends.oracle'`. 그외에 [서드파티 백엔드](https://docs.djangoproject.com/ko/3.2/ref/databases/#third-party-notes) 참조.



저는 mysql을 불러올꺼기 때문에 엔진을 `'django.db.backends.mysql'`라고 하고 데이터의 이름 `tip`, user에 `root`, 비밀번호, HOST, PORT를 그림과 같이 작성합니다. 

![image-20210623010005576](readme.assets/image-20210623010005576.png)

참고 : https://docs.djangoproject.com/en/3.2/ref/settings/#databases



기본 어플리케이션들 중 몇몇은 최소한 하나 이상의 데이터베이스 테이블을 사용하는데, 그러기 위해서는 데이터베이스에서 테이블을 미리 만들 필요가 있습니다. 이를 위해, 다음의 명령을 실행해봅시다.

```shell
$ python manage.py migrate
```



MySQL에서 새로고침? 버튼을 누르면 아래와 같이 테이블을 불러온 것을 확인할 수 있습니다.

![image-20210623010621125](readme.assets/image-20210623010621125.png)



단, MysQL이 연결이 안되는 에러가 발생했을경우에는

- 시작버튼을 눌러 서비스를 검색하고 클릭

- MySQL80을 찾아서 우클릭후 시작버튼을 누르면 됩니다.

![image-20210623010844048](readme.assets/image-20210623010844048.png)





## Superuser 만들기

https://kamang-it.tistory.com/entry/Django-02superuser-%EB%A7%8C%EB%93%A4%EA%B8%B0



django에서는 특정 프로젝트에 대해서 user그룹이란게 존재한다.

마치 db의 user와 유사하고 실제로도 그렇다.

맨처음에 유저는 존재치 않는다.

따라서 user를 만들어줘야할 필요성이 있는것이다.

```shell
python manage.py createsuperuser
```

위의 명령어를 사용하면 해당 프로젝트에서 superuser(흔히 말하는 root계정)을 만들 수 있다.

여기서 당신의 이름과 메일, 그리고 패스워드를 입력해주면 완성된다.

![image-20210623011513716](readme.assets/image-20210623011513716.png)



참고로 비밀번호 입력시 보이지 않으며 패스워드가 너무짧으면 Bypass~? [y/N]가 나오는데 y로 하면 짧은대로 된다.

http://127.0.0.1:8000/admin/



vs code command prompt에서 아래 코드를 작성한다.

```
python manage.py runserver 
```

![image-20210623012822093](readme.assets/image-20210623012822093.png)



여기로 들어가게 되면 아래와 같은 화면이 나오고 User을 클릭한다.

![image-20210623012430203](readme.assets/image-20210623012430203.png)

add user을 누르고 

![image-20210623012517271](readme.assets/image-20210623012517271.png)



새로운 username과 password를 작성했다.

![image-20210623012618645](readme.assets/image-20210623012618645.png)

나의경우 me로 작성했는데 아래와 같이 생성된것을 확인할 수 있다.

![image-20210623013048666](readme.assets/image-20210623013048666.png)



