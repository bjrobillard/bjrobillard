import { render, screen } from '@testing-library/react';
import App from './App';

test('renders table for numbers', () => {
  render(<App />);
  expect(screen.getByTestId('tableTest')).toHaveClass('App');
});
