import {render, screen} from '@testing-library/react';
import CountingGos from './CountingGos';

test('Amount of #\'s put in... ', () => {
    render(<CountingGos />);
    expect(screen.getByTestId('amtTestID')).toHaveClass('amt');
});