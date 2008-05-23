class IsoCollision:
    
    def __init__(self):
        pass
    
    def point_in(self, edges, point):
        output = False
        
        #A
        func_a = lambda x: (-0.58 *x) + (edges[0][1]-(-0.58 * edges[0][0]))
        res_a = func_a(point[0])
        a = point[1] < res_a  
        
        #B
        func_b = lambda x: (0.58 *x) + (edges[1][1]-(0.58 * edges[1][0]))
        b = point[1] > func_b(point[0])
        
        #C
        func_c = lambda x: (0.58 *x) + (edges[2][1]-(0.58 * edges[2][0]))
        c = point[1] > func_c(point[0])
        
        #D
        func_d = lambda x: (-0.58 *x) + (edges[3][1]-(-0.58 * edges[3][0]))
        d = point[1] < func_d(point[0])
        
        return a and b and c and d

    def collision(self, sprite1, sprite2):
        r1 = sprite1.rect
        r2 = sprite2.rect
        edges1 = [
                  [r1[0]+(r1[2]/2) , r1[1]+r1[3]],
                  [r1[0], r1[1]+(r1[3]/2)],
                  [r1[0]+(r1[2]/2) ,r1[1]],
                  [r1[0]+r1[2] , r1[1]+(r1[3]/2)],
                 ]
        edges2 = [
                  [r2[0]+(r2[2]/2) , r2[1]+r2[3]],
                  [r2[0], r2[1]+(r2[3]/2)],
                  [r2[0]+(r2[2]/2) ,r2[1]],                  
                  [r2[0]+r2[2] , r2[1]+(r2[3]/2)],
                 ]

        print r1
        print edges1
        
        
        for edge in edges1:
            if self.point_in (edges2, edge):
                return True
        return False

def main():
    edges = [[100,116],[0, 58],[100,0],[200,58]]
    point = [150,100]
    iso = IsoCollision()
    result = iso.point_in(edges, point)
    print result
                

if __name__ == '__main__': main()