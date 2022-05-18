import {render, screen} from '@testing-library/react';
import Author from './Author';

test('Author is in the document', () => { //make sure author is in the document
    render(<Author />);
    const author = screen.getByText("By: Ben Robillard");
    expect(author).toBeInTheDocument();
});