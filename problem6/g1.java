import java.util.*;

public class G{

    static int n;
    static ArrayList<ArrayList<Pair>> adj = new ArrayList<ArrayList<Pair>>();
    static int[] Pair_U, Pair_V, Dist;
    static final int NIL = 0, INF = Integer.MAX_VALUE;

    static class Pair {
        int first, second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }

    //Is Correct
    public static boolean bfs(int k)
    {
        Queue<Integer> Q = new LinkedList<Integer>();

        for(int i=1; i<=n; i++)
        {
            if(Pair_U[i] == NIL)
            {
                Dist[i] = 0;
                Q.add(i);
            }
            else Dist[i] = INF;
        }
        Dist[NIL] = INF;

        while(!Q.isEmpty())
        {
            int u = Q.poll();

            if(Dist[u] < Dist[NIL])
            {
                for(Pair c: adj.get(u))
                {
                    int v = c.first, p = c.second;
                    if(p <= k && Dist[Pair_V[v]] == INF)
                    {
                        Dist[Pair_V[v]] = Dist[u] + 1;
                        Q.add(Pair_V[v]);
                    }
                }
            }
        }

        return Dist[NIL] != INF;
    }

    //Is Correct
    public static boolean dfs(int u, int k)
    {
        if(u != NIL)
        {
            for(Pair c: adj.get(u))
            {
                int v = c.first, p = c.second;
                if(p <= k && Dist[Pair_V[v]] == Dist[u] + 1)
                {
                    if(dfs(Pair_V[v], k))
                    {
                        Pair_V[v] = u;
                        Pair_U[u] = v;
                        return true;
                    }
                }
            }
            Dist[u] = INF;
            return false;
        }
        return true;
    }

    //Is Correct
    //Modified Hopcroft - Karp (See Ed Discussion for more info)
    public static boolean HK(int k)
    {
        int cnt = 0;

        Pair_U = new int[n+1];
        Pair_V = new int[n+1];
        Dist = new int[n+1];

        while(bfs(k))
        {
            for(int i=1; i<=n; i++)
            {
                if(Pair_U[i] == NIL && dfs(i, k)) cnt++;
            }
        }

        return cnt == n;
    }

    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);

        n = s.nextInt();
        int m = s.nextInt();

        for(int i = 0; i <= n; i++) 
        {
            adj.add(new ArrayList<Pair>());
        }

        int[][] edge = new int[m][3];
        for(int i=0; i<m; i++)
        {
            edge[i][1] = s.nextInt();
            edge[i][2] = s.nextInt();
            edge[i][0] = s.nextInt();
        }
        Arrays.sort(edge, (a, b) -> a[0] - b[0]);

        s.close();

        for(int i=0; i<m; i++)
        {
            int u = edge[i][1], v = edge[i][2];
            adj.get(u).add(new Pair(v, i));
        }

        int l = 0;
        int r = m;

        while (l < r)
        {
            int mid = (l + r) / 2;
            if(HK(mid)){
                r = mid;
            }
            else {
                l = mid + 1;
            }

        }
        if(l < m) System.out.println(edge[l][0]);
        else System.out.println(-1);
    }
}

