import numpy as np
import open3d as o3d
import pptk
class CMulPoints:
    def __init__(self, file):
        self.file =file

    def pick_points(self, pcd):
        vis = o3d.visualization.VisualizerWithEditing()
        vis.create_window()
        vis.add_geometry(pcd)
        vis.run()
        vis.destroy_window()
        return vis.get_picked_points()

    def vektor(self,tablica,iloscPKT):
        P = np.array(tablica)
        P1 = (P[0, 0], P[0, 1], P[0, 2])
        P2 = (P[1, 0], P[1, 1], P[1, 2])
        x= P2[0]-P1[0]
        y= P2[1]-P1[1]
        z= P2[2]-P1[2]
        dx=x/(int(iloscPKT)+1)
        dy=y/(int(iloscPKT)+1)
        dz=z/(int(iloscPKT)+1)
        X = []
        iter=1
        while iter <= int(iloscPKT):
            X.append([P[0, 0] + dx*iter, P[0, 1] + dy*iter, P[0, 2] + dz*iter])
            iter=iter+1
        with open(self.file, 'a+') as file:
            for line in X:
                word = (str(line)).replace(',', '')
                word = (str(word)).replace(']', '')
                word = (str(word)).replace('[', '')
                file.write(str(word) + "\n")
    def run (self, liczbaPKT):

        print("Load a ply point cloud, print it, and render it")
        pcd = o3d.io.read_point_cloud(self.file)
        print(pcd)
        print(np.asarray(pcd.points))
        V = self.pick_points(pcd)
        tab = []
        for nr_pkt in V:
            i=0
            with open(self.file) as plik:
                for wiersz in plik:
                    if nr_pkt==i:
                        tab.append(list(map(float, wiersz.split(' '))))
                    i = i + 1
        self.vektor(tab, liczbaPKT)


        with open(self.file) as plik:
            tab1 = [list(map(float, wiersz.split(' '))) for wiersz in plik]

        P1 =np.array(tab1)
        v = pptk.viewer(P1)
        v.set(point_size=0.1)
