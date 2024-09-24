import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")  # ウィンドウタイトル
    screen = pg.display.set_mode((800, 600))  # ウィンドウサイズ
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 背景画像
    bg_img_fl = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")  # こうかとん画像
    kk_img = pg.transform.flip(kk_img, True, False)  # こうかとん画像を左右反転
    kk_rct = kk_img.get_rect()  # RECT情報を取得
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr
        x = x%3200
        # 背景
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_fl, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        # screen.blit(bg_img_fl, [-x+4800, 0])  # 4枚目は無くても動く
        # こうかとん
        screen.blit(kk_img, move(kk_rct))  # move関数を使用
        pg.display.update()
        tmr += 1        
        clock.tick(200)


def move(rct):
    key_lst = pg.key.get_pressed()
    # move_key = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]
    if key_lst[pg.K_UP]:
        rct.move_ip(0, -1)
    elif key_lst[pg.K_DOWN]:
        rct.move_ip(0, 1)
    elif key_lst[pg.K_LEFT]:
        rct.move_ip(-1, 0)
    elif key_lst[pg.K_RIGHT]:
        rct.move_ip(2, 0)
    else:
        rct.move_ip(-1, 0)
    return rct

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()