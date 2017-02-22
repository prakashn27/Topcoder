public class TestTaking {

	public int findMax(int questions, int guessed, int actual) {
		int res = 0;
		
		int wrong = Math.abs(guessed - actual);
		res = questions - wrong;
		return res;
	}

}
