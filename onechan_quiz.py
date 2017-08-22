score = 0 
comics = ['NEW GAME!','がっこうぐらし！','ご注文はうさぎですか？','うらら迷路帖']
answers = [3,2,1,4]
#問題
for i in range(1,5):
    print('問題{}　{}に出てくるお姉ちゃんはだれ？ \n 1.保登モカ 2.佐倉慈 3.遠山りん 4.棗ニナ \n 数字で解答>>>'.format(i,comics[i-1]))
    sister = input()
    if sister == str(answers[i-1]):
        score += 100
#成績発表
if score == 400:
    print('全問正解！！')
elif score == 0 :
    print('不合格！')
else :
    print('{}問正解！'.format(int(score/100)))