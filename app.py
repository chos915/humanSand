# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import datetime
from PIL import Image

def main():
    """코드 작성"""

    st.title("Hello World")

    st.text('this is {}'.format('good'))

    st.header('This is header')

    st.subheader('This is sub Header')

    st.markdown('## This Markdown Header')

    # Colored Text
    st.success('성공')
    st.warning('위험함')
    st.info('This is information')
    st.exception('This is an exception')

    # 수퍼펑션
    st.write(1+1)
    st.write(type("normal"))

    a = 1
    b = 2
    st.write(a + b)

    st.write(dir(str))
    st.help(range)

    iris = pd.read_csv("data/iris.csv")
    st.dataframe(iris, 200, 100)

    # 색상 추가
    st.title('Adding Color on Table')
    st.dataframe(iris.style.highlight_max(axis=0))

    # static table show
    st.table(iris.head(30))

    # st.write
    st.write(iris)

    # 나의 코드 보여주기
    myCode = """
    def hello():
        print("Hello World!")
    """
    st.code(myCode, language = 'Python')

    ## Widgets, 버튼, 체크박스
    name = "Wifi"

    if st.button('Submit'):
        st.write(f'name: {name.upper()}')
    
    if st.button('Submit', key = 'new02'): #같은 버튼이 여러개 있는 경우 key 값을 사용한다.
        st.write(f'name: {name.lower()}')

    # Radio button
    status = st.radio("Status", ("활성화","비활성화"))
    st.write(status)
    if status == "활성화":
        st.success("활성화 상태")
    elif status == "비활성화":
        st.info("비활성화 상태")
    else:
        pass

    # Check Box
    if st.checkbox("Show/Hide"):
        st.text('보여줘!')
    
    d = st.date_input(
        "When\'s your birthday",
        datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)    # datetime 실행시 에러발생 --> 맨 윗줄에 import datetime 적었는지 확인

    # selectbox
    programings = ['Python','Java', 'HTML', 'CSS', 'JS']
    choice = st.selectbox('프로그래밍 언어:', programings)
    st.write(f'{choice}언어를 선택함')

    # Multiple Selection
    spoken_lang = ("영어", "일본어", "중국어", "독일어")
    mylangchoice = st.multiselect("언어 선택", spoken_lang, default = "영어")
    st.write("선택:",mylangchoice)

    # Slider
    age = st.slider('나이', 1, 120)
    st.write(age)

    
    color = st.select_slider('색상-선택:',
                             options = ['노란색', '빨간색','파란색','검정색','흰색'],
                             value = ("노란색", "흰색")) 
    st.write(color)
    
    """
    start_color, end_color = st.select_slider('색상-선택:',
                             options = ['노란색', '빨간색','파란색','검정색','흰색'],
                             value = ("노란색", "흰색")) 
    st.write(start_color, end_color)
    """

    ## 멀티 미디어 파일
    img = Image.open('data/image_03.jpg')
    st.image(img)

    img_url = 'https://esther.wisacdn.com/board//_data/basic_9/202202/23/e4356b1e337ac31d5faad06a71be95ff.jpg'   # 구글에 넣고싶은 이미지 검색후 이미지 마우스 우클릭 후 이미지 주소 복사 클릭해서 붙여넣기
    st.image(img_url)

    # 비디오 출력
    # 컨텍스트 매니저(Context Manager) : 특정 작업의 시작과 끝에 정해진 행동을 수행할 수 있도록 한다. 
    #__enter__은 컨텍스트의 시작에서 수행할 작업을, __exit__는 컨텍스트가 종료될 때 수행되는 코드를 담고 있다.
    with open('data/secret_of_success.mp4', 'rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time = 1)

    # 오디오 출력
    with open('data/song.mp3', 'rb') as rb:
        audio_file = rb.read()
        st.audio(audio_file, format='audio/mp3')

    # 유튜브 비디오 출력
    st.video('https://www.youtube.com/watch?v=MFJOYHM39yo')
    
    # text
    fname = st.text_input('입력해주세요')
    st.title(fname)

    message = st.text_area('입력해주세요', height = 300)
    st.write(message)

    nums = st.number_input('숫자 입력')
    st.write(nums)

    mytime = st.time_input('시간')
    st.write(mytime)

    # color Picker
    color = st.color_picker('색상 선택')
    st.write(color)

if __name__ == "__main__":
    main()
