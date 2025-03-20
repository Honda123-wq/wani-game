import pygame

# Pygameの初期化
pygame.mixer.init()

# 音声ファイルのロード
correct_sound = pygame.mixer.Sound("sounds/correct.mp3")
wrong_sound = pygame.mixer.Sound("sounds/wrong.mp3")

#正解のときの音を鳴らす
def play_correct():
    correct_sound.play()

#間違いのときの音を鳴らす
def play_wrong():
    wrong_sound.play()

#テスト用（このファイルを直接実行したときに音が鳴る）
if __name__ == "__main__":
    user_input = input("正解なら1、間違いなら0を入力してね: ")
    if user_input == "1":
        play_correct()
    else:
        play_wrong()

    input("Enterキーを押すと終了します")
