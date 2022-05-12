import { render, screen } from '@testing-library/react';
import App from './App';

// test('renders learn react link', () => {
//   render(<App />);
//   const linkElement = screen.getByText(/learn react/i);
//   expect(linkElement).toBeInTheDocument();
// });

test('renders table for numbers', () => {
  render(<App />);
  expect(screen.getByTestId('tableTest')).toHaveClass('App');
});
