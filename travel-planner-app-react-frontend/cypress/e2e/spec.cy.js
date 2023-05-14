describe('Add Trip (without auth)', () => {
  it('should be able to fill in the Add Trip form but failed on submit', () => {
    cy.visit('http://127.0.0.1:3000')

    // Click the "Trips" link in the menu
    cy.contains('a', 'Trips').click()

    // Click the "Add Trip" button
    cy.contains('button', 'Add Trip').click()

    // Fill in the form fields
    cy.get('input[name="name"]').type('My Trip')
    cy.get('input[name="destination"]').type('MyDestination')
    cy.get('input[name="start_date"]').type('2023-05-30')
    cy.get('input[name="end_date"]').type('2023-06-03')
    cy.get('input[name="budget"]').type('1000')
    cy.get('textarea[name="notes"]').type('This is a note.')

    // Click the "Create Trip" button
    cy.contains('button', 'Create Trip').click()

    // Check if the error message appears
    cy.get('div').should('contain', 'Authentication credentials were not provided.')
  })
})

describe('Add Trip (with auth)', () => {
  it('should be able to navigate to the Add Trip form after logging in', () => {
    cy.visit('http://127.0.0.1:3000')

    // Click the "Login" button
    cy.contains('a', 'Login').click()

    // Enter the username and password
    cy.get('input[name="username"]').type('BarryHary')
    cy.get('input[name="password"]').type('cababa20011215')

    // Click the "Submit" button
    cy.get('button[type="submit"]').click()

    // Check if we see the Home Page after submitting the form
    cy.url().should('eq', 'http://127.0.0.1:3000/') // Assert that the URL matches the Home Page URL


    // Wait for the "Add Trip" button to appear and click on it
    cy.wait(1000) // Adjust the wait time as needed

    // Click the "Trips" link in the menu
    cy.contains('a', 'Trips').click()


    cy.contains('button', 'Add Trip').click()

    // Fill in the form fields
    cy.get('input[name="name"]').type('My Trip')
    cy.get('input[name="destination"]').type('MyDestination')
    cy.get('input[name="start_date"]').type('2023-05-30')
    cy.get('input[name="end_date"]').type('2023-06-03')
    cy.get('input[name="budget"]').type('1000')
    cy.get('textarea[name="notes"]').type('This is a note.')

    // Click the "Create Trip" button
    cy.contains('button', 'Create Trip').click()

    cy.url().should('eq', 'http://127.0.0.1:3000/trips/') // Assert that the URL matches the Trip Page URL
    cy.get('div').should('contain', 'Trip has been created successfully.')
  })
})
