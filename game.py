import sys, pygame
pygame.init()

footbal_image_name = "footbal.png"
footbal_image = pygame.image.load(footbal_image_name)
footbal_image_size = footbal_image.get_size()


sc = pygame.display.set_mode(footbal_image_size)
pygame.display.set_caption("мая первая игра")
pygame.display.set_icon(footbal_image)
pygame.draw.rect(sc, (255,255,255), (10,10,50,100))

while True:
    sc.blit(footbal_image, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
           
    pygame.display.update()