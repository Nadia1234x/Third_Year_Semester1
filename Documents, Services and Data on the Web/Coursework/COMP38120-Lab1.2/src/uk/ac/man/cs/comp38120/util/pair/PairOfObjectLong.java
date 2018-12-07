/*
 * Cloud9: A MapReduce Library for Hadoop Licensed under the Apache License,
 * Version 2.0 (the "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 * http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law
 * or agreed to in writing, software distributed under the License is
 * distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 */

package uk.ac.man.cs.comp38120.util.pair;

public class PairOfObjectLong<L extends Comparable<L>> implements
        Comparable<PairOfObjectLong<L>>
{

    private L left;
    private long right;

    public PairOfObjectLong(L left, long right)
    {
        this.left = left;
        this.right = right;
    }

    public PairOfObjectLong()
    {
    }

    public L getLeftElement()
    {
        return left;
    }

    public long getRightElement()
    {
        return right;
    }

    public void set(L left, long right)
    {
        this.left = left;
        this.right = right;
    }

    public void setLeftElement(L left)
    {
        this.left = left;
    }

    public void setRightElement(long right)
    {
        this.right = right;
    }

    /**
     * Generates human-readable String representation of this pair.
     */
    public String toString()
    {
        return "(" + left + ", " + right + ")";
    }

    /**
     * Creates a shallow clone of this object; the left element itself is not
     * cloned.
     */
    public PairOfObjectLong<L> clone()
    {
        return new PairOfObjectLong<L>(left, right);
    }

    @Override
    public int compareTo(PairOfObjectLong<L> that)
    {
        if (this.left.equals(that.left))
        {
            return that.right > this.right ? -1 : 1;
        }
        return this.left.compareTo(that.left);
    }
}
