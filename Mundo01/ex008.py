d = float(input('Digite uma distancia em metros: '))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d *1000
print('A distância de {} metros corresponde à:'.format(d))
print('{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'.format(km, hm, dam, dm, cm, mm))
