public class main{
    

    public void Ganador(){

    }

    public void Pintar(){
        System.out.print("   ABC\n");
        for (int i=0; i<3; i++){
            System.out.print(i+": ");
            for(int j=0; j<3; j++){
                System.out.print(Matriz[i][j]);
            }
            
            System.out.print("\n");
        }
    }

    public static void main(String[] args){
        //int[][] Matriz = new int[3][3];
        int Matriz[][] = {
            {0,0,0},
            {0,0,0},
            {0,0,0}
        };

        Pintar();
    }
}