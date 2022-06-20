import java.util.Arrays;

class testing {

  public static String missingChar(String str, int n) {
    String[] broken = str.split("");
    String fini = "";
    for (int i = 0; i < broken.length; i++) {
      if (i != n) {
        fini = fini + broken[i];
      }

    }
    return fini;

  }

  public boolean scoresIncreasing(int[] scores) {
    int current = scores[0];

    for (int i = 1; i < scores.length; i++) {
      if (current <= scores[i]) {
        current = scores[i];

      } else {
        return false;
      }

    }
    return true;
  }

  public String[] wordsFront(String[] words, int n) {
    String[] fini = new String[n];
    for (int i = 0; i < fini.length; i++) {
      fini[i] = words[i];
    }
    return fini;
  }

  public int scoreUp(String[] key, String[] answers) {
    int score = 0;
    for (int i = 0; i < answers.length; i++) {
      if (key[i] == answers[i]) {
        score += 4;

      } else if (key[i] != answers[i] && answers[i] != "?") {
        score--;

      }
    }
    return score;
  }

  public static int bigHeights(int[] heights, int start, int end) {
    int steps = 0;
    int[] trail = new int[Math.abs(end - start + 1)];
    for (int i = 0; i < trail.length; i++) {
      trail[i] = heights[i + start];
    }
    int current = heights[start];
    for (int i = 0; i < (trail.length - 1); i++) {
      if (Math.abs(current - trail[i + 1]) >= 5) {
        steps++;

      }
      current = trail[i + 1];

    }
    System.out.println(Arrays.toString(trail));
    return steps;
  }

  public int userCompare(String aName, int aId, String bName, int bId) {
    if (aName.compareTo(bName) > 0) {
      return 1;
    } else if (aName.compareTo(bName) < 0) {
      return -1;
    } else if (aName.compareTo(bName) == 0) {
      if (aId > bId) {
        return 1;
      } else if (aId < bId) {
        return 0;
      } else {
        return 0;
      }

    }

    return 0;
  }

  public String[] mergeTwo(String[] a, String[] b, int n) {
    
  }

  public static void main(String[] args) {
    System.out.println("testing".compareTo("testing"));
  }
}
