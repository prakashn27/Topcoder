import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class TestTakingTest {

    protected TestTaking solution;

    @Before
    public void setUp() {
        solution = new TestTaking();
    }

    @Test(timeout = 2000)
    public void testCase0() {
        int questions = 3;
        int guessed = 1;
        int actual1 = 2;

        int expected = 2;
        int actual = solution.findMax(questions, guessed, actual1);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase1() {
        int questions = 3;
        int guessed = 2;
        int actual1 = 1;

        int expected = 2;
        int actual = solution.findMax(questions, guessed, actual1);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase2() {
        int questions = 5;
        int guessed = 5;
        int actual1 = 0;

        int expected = 0;
        int actual = solution.findMax(questions, guessed, actual1);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase3() {
        int questions = 10;
        int guessed = 8;
        int actual1 = 8;

        int expected = 10;
        int actual = solution.findMax(questions, guessed, actual1);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase4() {
        int questions = 7;
        int guessed = 0;
        int actual1 = 2;

        int expected = 5;
        int actual = solution.findMax(questions, guessed, actual1);

        Assert.assertEquals(expected, actual);
    }

}
