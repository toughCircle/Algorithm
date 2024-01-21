import static java.util.Arrays.sort;

class Solution {
    public int solution(int[] array) {
        
        sort(array);

        int answer = array[array.length / 2];
        return answer;
    }
}