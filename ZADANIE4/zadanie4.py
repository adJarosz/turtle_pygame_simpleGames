# - jaki model został użyty: ChatGPT (model GPT-5.2)
# - treść wszystkich promptów napisanych aż do uzyskania
# poprawnego rezultatu, czyli poniższego działającego kodu!:
#1. Wygeneruj jak najkrótszy kod w języku python, korzystając wyłącznie z biblioteki pygame.
#   Kod ma być programem do rysowania myszką typu paint, ale z ograniczonymi funkcjonalnościami.
#   Ma pozwalać wyłącznie na: wybór kolorów i grubości pisaka oraz ma posiadać opcję czyszczenia ekranu.
#   Ma wyglądać tak jak na dodanym obrazku poglądowym

#2. Dodaj obwódkę, aby było widać jaki kolor i jaka grubość pędzla aktualnie jest zaznaczona
#   oraz zmniejsz przestrzeń pomiędzy kolorami w palecie kolorów


import pygame as p
p.init();W,H=1200,700
s=p.display.set_mode((W,H));f=p.font.SysFont(None,32)
cols=[(255,0,0),(255,100,0),(255,220,0),(0,180,0),(0,160,255),(0,0,180),(150,0,180)]
bs=[22,14,8,3]
pal=[(40+i*55,80) for i in range(len(cols))]
brc=[(520+i*70,80) for i in range(len(bs))]
clr=p.Rect(1000,55,60,60)
g=p.Surface((W,H));g.fill((255,255,255))
c=cols[0];b=bs[0];draw=0
def ui():
    s.blit(g,(0,0))
    s.blit(f.render("PALETA KOLORÓW",1,(0,0,0)),(20,20))
    s.blit(f.render("GRUBOŚĆ PĘDZLA",1,(0,0,0)),(480,20))
    s.blit(f.render("WYCZYŚĆ EKRAN",1,(0,0,0)),(950,20))
    for i,(x,y) in enumerate(pal):
        if cols[i]==c:p.draw.circle(s,(0,0,0),(x,y),26,3)
        p.draw.circle(s,cols[i],(x,y),20)
    for i,(x,y) in enumerate(brc):
        if bs[i]==b:p.draw.circle(s,(0,150,255),(x,y),bs[i]+6,3)
        p.draw.circle(s,(0,0,0),(x,y),bs[i])
    p.draw.rect(s,(0,0,0),clr,2)
while 1:
    for e in p.event.get():
        if e.type==p.QUIT:quit()
        if e.type==p.MOUSEBUTTONDOWN:
            m=p.mouse.get_pos()
            if m[1]<140:
                for i,(x,y) in enumerate(pal):
                    if (m[0]-x)**2+(m[1]-y)**2<400:c=cols[i]
                for i,(x,y) in enumerate(brc):
                    if (m[0]-x)**2+(m[1]-y)**2<bs[i]**2:b=bs[i]
                if clr.collidepoint(m):g.fill((255,255,255))
            else:draw=1
        if e.type==p.MOUSEBUTTONUP:draw=0
    if draw and p.mouse.get_pressed()[0]:
        p.draw.circle(g,c,p.mouse.get_pos(),b)
    ui();p.display.flip()

