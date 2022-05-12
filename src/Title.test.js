import {render, screen} from '@testing-library/react';
import Title from './Title';

test('Title is in the document', () => { //make sure title is in the document
    render(<Title />);
    const title = screen.getByText("The Magic Square");
    expect(title).toBeInTheDocument();
}) 
