import java.util.ArrayList;
import java.util.List;



class Solution {
    public int[] solution(int n) {
        
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
          if (i % 2 != 0) {
            list.add(i);
          }
        }
        
        int[] answer = list.stream().mapToInt(i -> i).toArray();
        
        
        return answer;
    }
}