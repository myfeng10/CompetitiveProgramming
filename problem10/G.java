import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class G{
    public static final long INF = (long) 1e18;
    public static int n, MAXN = 200000;
    public static long[] t = new long[4*MAXN], lazy = new long[4*MAXN];

    public static void build(long[]a, int v, int tl, int tr) {
        if (tl == tr) {
            t[v] = a[tl];
        } else {
            int tm = (tl + tr) / 2;
            build(a, v*2, tl, tm);
            build(a, v*2+1, tm+1, tr);
            t[v] = Math.min(t[v*2], t[v*2 + 1]);
        }
    }

    public static void push(int v) {
        t[v*2] += lazy[v];
        lazy[v*2] += lazy[v];
        t[v*2+1] += lazy[v];
        lazy[v*2+1] += lazy[v];
        lazy[v] = 0;
    }

    public static void update(int v, int tl, int tr, int l, int r, long addend) {
        if (l > r)
            return;
        if (l == tl && tr == r) {
            t[v] += addend;
            lazy[v] += addend;
        } else {
            push(v);
            int tm = (tl + tr) / 2;
            update(v*2, tl, tm, l, Math.min(r, tm), addend);
            update(v*2+1, tm+1, tr, Math.max(l, tm+1), r, addend);
            t[v] = Math.min(t[v*2], t[v*2+1]);
        }
    }

    public static long query(int v, int tl, int tr, int l, int r) {
        if (l > r)
            return INF;
        if (l == tl && tr == r)
            return t[v];
        push(v);
        int tm = (tl + tr) / 2;
        return Math.min(query(v*2, tl, tm, l, Math.min(r, tm)),
                query(v*2+1, tm+1, tr, Math.max(l, tm+1), r));
    }

    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        long[] a = new long[n];

        for(int i=0; i<n; i++) a[i] = s.nextInt();

        build(a, 1, 0, n-1);

        int q = s.nextInt();
        s.nextLine();
        while(q-->0)
        {
            String str = s.nextLine();

            String[] strings = str.split(" ");

            List<Integer> param = Stream.of(strings).
                                map(value -> Integer.valueOf(value)).
                                collect(Collectors.toList());

            if(param.size()==2)
            {
                int l = param.get(0), r = param.get(1);
                if(r < l) {
                    if (query(1,0,n-1,0,r)<query(1,0,n-1,l,n-1))
                        System.out.println(query(1, 0, n-1, 0, r));
                    else
                        System.out.println(query(1, 0, n-1, l, n-1));
                }
                else
                    System.out.println(query(1, 0, n-1, l, r));
            }
            else
            {
                int l = param.get(0), r = param.get(1), v = param.get(2);
                if(r < l)
                {
                    update(1,0,n-1,1,n-1,v);
                    update(1,0,n-1,0,r,v);
                }
                else
                {
                    update(1, 0, n-1, l, r, v);
                }
            }
        }
    }
}
