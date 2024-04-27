import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader;
import java.util.*;

public class G
{
    static class FastReader { 
        BufferedReader br; 
        StringTokenizer st; 
  
        public FastReader() 
        { 
            br = new BufferedReader( 
                new InputStreamReader(System.in)); 
        } 
  
        String next() 
        { 
            while (st == null || !st.hasMoreElements()) { 
                try { 
                    st = new StringTokenizer(br.readLine()); 
                } 
                catch (IOException e) { 
                    e.printStackTrace(); 
                } 
            } 
            return st.nextToken(); 
        } 
  
        int nextInt() { return Integer.parseInt(next()); } 
  
        long nextLong() { return Long.parseLong(next()); } 
  
        double nextDouble() 
        { 
            return Double.parseDouble(next()); 
        } 
  
        String nextLine() 
        { 
            String str = ""; 
            try { 
                if(st.hasMoreTokens()){ 
                    str = st.nextToken("\n"); 
                } 
                else{ 
                    str = br.readLine(); 
                } 
            } 
            catch (IOException e) { 
                e.printStackTrace(); 
            } 
            return str; 
        } 
    } 

    //Sieve of Eratosthenes
    private static int n = 10000000;
    private static boolean[] isPrime = new boolean[n + 1];
    private static int[] num = new int[n + 1];

    static class Pair {
        int first, second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }

    private static void sieve()
    {
        for(int i=0; i<n+1; i++) isPrime[i] = true;
        for(int i=2; i<=n; i++){ 
            if(isPrime[i]){ 
                for(int j=2*i; j<=n; j+=i){
                    if (num[j] == 0) num[j] = i;
                    isPrime[j] = false;
                }
            }
        }
    }

    public static void main(String args[])
    {
        FastReader s = new FastReader();
        sieve();

        int n = s.nextInt();

        int[] a = new int[n];
        int[] d1 = new int[n];
        int[] d2 = new int[n];

        HashMap<Integer, Pair> D = new HashMap<>();

        for(int i=0; i<n; i++)
        {
            int y = s.nextInt();
            a[i] = y;

            if(isPrime[a[i]]) { 
                d1[i] = d2[i] = -1;
            } else {
                int x = a[i];
                int cnt = 0;
                int firstPrimeDivisor = num[a[i]]; // Get the smallest prime divisor

                // Calculate the highest power of the smallest prime divisor that still divides a[i]
                while(x % firstPrimeDivisor == 0) {
                    cnt++;
                    x /= firstPrimeDivisor;
                }

                if(x == 1) { // If the remaining quotient is 1, no valid divisors exist
                    d1[i] = d2[i] = -1;
                } else {
                    d1[i] = (int)Math.pow(firstPrimeDivisor, cnt); // Calculate d1
                    d2[i] = x; // Calculate d2
                }
            }
        }
        for (int i = 0; i < n; i++) System.out.print(d1[i] + " ");
        System.out.println();
        for (int i = 0; i < n; i++) System.out.print(d2[i] + " ");
        System.out.println();


    }
}