
class Solution {
    public int[] solution(int[] numbers) {
        
        int[] answer = new int[numbers.length];

        int ans = 0;

        for (int i = 0; i < numbers.length; i++) {
            ans = numbers[i] * 2;
            answer[i] = ans;
        }
        
        return answer;
    }
}