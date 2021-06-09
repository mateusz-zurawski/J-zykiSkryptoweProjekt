import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

class CWayCreator:
    def __init__(self,src_file,dest_file):
        self.src_file = src_file
        self.des_file =dest_file

    def pick_points(self,pcd):
        print("")
        print("1) Please pick at least three correspondences using [shift + left click]")
        print("   Press [shift + right click] to undo point picking")
        print("2) Afther picking points, press q for close the window")
        vis = o3d.visualization.VisualizerWithEditing()
        vis.create_window()
        vis.add_geometry(pcd)
        vis.run()
        vis.destroy_window()
        return vis.get_picked_points()

    def run(self):
        print("Load a ply point cloud, print it, and render it")
        pcd = o3d.io.read_point_cloud(self.src_file)
        print(pcd)
        print(np.asarray(pcd.points))
        V = self.pick_points(pcd)
        print ("---Queue---")
        tab = []
        for nr_pkt in V:
            i=0
            with open(self.src_file) as plik:
                    for wiersz in plik:
                        if nr_pkt==i:
                            tab.append(list(map(float, wiersz.split(' '))))
                            print(wiersz)
                        i = i + 1


        with open(self.des_file, 'w') as file:
                for line in tab:
                    word = (str(line)).replace(',', '')
                    word = (str(word)).replace(']', '')
                    word = (str(word)).replace('[', '')
                    file.write(str(word) + "\n")





        with open(self.des_file) as plik:
            tab = [list(map(float, wiersz.split(' '))) for wiersz in plik]

        with open(self.src_file) as plik:
            tab2 = [list(map(float, wiersz.split(' '))) for wiersz in plik]

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        P=np.array(tab)
        z = P[:,2]
        x = P[:,0]
        y = P[:,1]
        ax.plot(x, y, z, label='created line')
        P2 = np.array(tab2)
        ax.scatter(P2[:,0], P2[:,1], P2[:,2], c='b', marker='v')
        ax.legend()
        plt.show()
