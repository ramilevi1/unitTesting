package pivotal;

import static org.junit.Assert.*;

import javax.naming.spi.DirStateFactory.Result;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import junit.extensions.TestSetup;

public class SetMainTest {
	
	// Req : Insert no element and see the size of the set
	@Test
	public void testSetEmpty(){
		SetMain setMain = new SetMain();
		assertEquals(0, setMain.size());
	}
	
	// Req : Insert 1 element and see the size of the set
	@Test
	public void testSetInsert1Element(){
		SetMain setMain = new SetMain();
		setMain.insert(1);
		assertEquals(1, setMain.size());
	}
	
	// Req : Insert multi elements and look at size
	@Test
	public void testSetInsertMultiElements(){
		SetMain setMain = new SetMain();
		for(int i=0; i < 10; i++){
			setMain.insert(i);
		}
		assertEquals(10, setMain.size());
	}
	
	// Req : Insert when more extrememly large elements
	@Test
	public void TestSetInsetExtremelyLarge(){
		int extremelyLargeInt = 100000;
		SetMain setMain = new SetMain(extremelyLargeInt);
		for(int i = 0; i< extremelyLargeInt; i++){
			setMain.insert(i);
		}
		assertEquals(extremelyLargeInt, setMain.size());
				
	}
	
	// Req : Insert multi elements with resizing
	@Test
	public void TestSetInsertMultiResizingInsert(){
		int sizeMarginallyHigher = 11;
		SetMain setMain = new SetMain();
		for(int i = 0; i<sizeMarginallyHigher; i++){
			setMain.insert(i);
		}
		assertEquals(sizeMarginallyHigher, setMain.size());
	}
	
	// Req : Contains for empty list
	@Test
	public void TestSetContainsEmptyList(){
		SetMain setMain = new SetMain();
		assertEquals(false, setMain.contains(1));
	}
	
	// Req : Contains? non existing element
	@Test
	public void TestSetContainsNonExistingElement(){
		int sizeMarginallyHigher = 11;
		SetMain setMain = new SetMain();
		for(int i = 0; i<sizeMarginallyHigher; i++){
			setMain.insert(i);
		}
		assertEquals(false, setMain.contains(14));
	}
	
	// Req : Contains for existing element
	@Test
	public void TestSetContainsExistingElement(){
		int sizeMarginallyHigher = 11;
		SetMain setMain = new SetMain();
		for(int i = 0; i<sizeMarginallyHigher; i++){
			setMain.insert(i);
		}
		assertEquals(true, setMain.contains(9));
	}
	
	// Req : delete from an empty list
	@Test
	public void TestSetDeleteEmptyList(){
		SetMain setMain = new SetMain();
		assertEquals(false, setMain.delete(11));	
		assertEquals(0, setMain.size());
	}
	
	// Req : Delete non existing element
	@Test
	public void TestSetDeleteNonExistingElement(){
		int sizeMarginallyHigher = 11;
		SetMain setMain = new SetMain();
		for(int i = 0; i<sizeMarginallyHigher; i++){
			setMain.insert(i);
		}
		assertEquals(false, setMain.delete(13));
	}
		
	// Req : Delete existing element
		@Test
		public void TestSetDeleteExistingElement(){
			int sizeMarginallyHigher = 11;
			SetMain setMain = new SetMain();
			for(int i = 0; i<sizeMarginallyHigher; i++){
				setMain.insert(i);
			}
			assertEquals(true, setMain.delete(10));
			assertEquals(10, setMain.size());
		}
		
		// Req : Insert duplicates
		@Test
		public void TestSetInsertDuplicates(){
			SetMain setMain = new SetMain();
			setMain.insert(1);
			setMain.insert(1);
			assertEquals(1, setMain.size());
		}
	
}
