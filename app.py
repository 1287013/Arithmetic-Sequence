import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The arithmetic sequence as a list of numbers
    """
    sequence = []
    for n in range(num_terms):
        term = first_term + (n * common_difference)
        sequence.append(term)
    return sequence

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title and description
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("""
    Generate arithmetic sequences by specifying the first term, common difference, and number of terms.
    
    **Formula:** aₙ = a₁ + (n-1)d
    - a₁ = first term
    - d = common difference
    - n = term position
    """)
    
    # Create input section
    st.header("Parameters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=1.0,
            help="The first number in the sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (max: 1000)"
        )
    
    # Input validation and sequence generation
    if st.button("Generate Sequence", type="primary"):
        try:
            # Convert num_terms to integer for validation
            num_terms = int(num_terms)
            
            if num_terms <= 0:
                st.error("Number of terms must be a positive integer.")
                return
            
            if num_terms > 1000:
                st.error("Number of terms cannot exceed 1000.")
                return
            
            # Generate the sequence
            sequence = generate_arithmetic_sequence(first_term, common_difference, num_terms)
            
            # Display results
            st.header("Results")
            
            # Show sequence info
            st.subheader("Sequence Information")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("First Term", f"{first_term}")
            with col2:
                st.metric("Common Difference", f"{common_difference}")
            with col3:
                st.metric("Number of Terms", f"{num_terms}")
            with col4:
                st.metric("Last Term", f"{sequence[-1]}")
            
            # Display the sequence
            st.subheader("Arithmetic Sequence")
            
            # Format sequence for display
            if num_terms <= 20:
                # Show all terms for small sequences
                sequence_str = ", ".join([str(term) for term in sequence])
                st.write(f"**Sequence:** {sequence_str}")
            else:
                # Show first 10 and last 10 terms for large sequences
                first_10 = sequence[:10]
                last_10 = sequence[-10:]
                first_str = ", ".join([str(term) for term in first_10])
                last_str = ", ".join([str(term) for term in last_10])
                st.write(f"**First 10 terms:** {first_str}")
                st.write(f"**Last 10 terms:** {last_str}")
                st.info(f"Showing first and last 10 terms of {num_terms} total terms")
            
            # Show as table for better readability
            st.subheader("Detailed View")
            
            # Create a table with term position and value
            table_data = []
            for i, term in enumerate(sequence[:50], 1):  # Limit table to first 50 terms
                table_data.append({
                    "Position (n)": i,
                    "Term (aₙ)": term,
                    "Calculation": f"{first_term} + ({i-1}) × {common_difference} = {term}"
                })
            
            st.dataframe(table_data, use_container_width=True)
            
            if num_terms > 50:
                st.info(f"Table shows first 50 terms of {num_terms} total terms")
            
            # Additional calculations
            st.subheader("Additional Information")
            sequence_sum = sum(sequence)
            average = sequence_sum / num_terms
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Sum of Sequence", f"{sequence_sum}")
            with col2:
                st.metric("Average Value", f"{average:.2f}")
            
            # Show the general formula for this specific sequence
            st.subheader("Formula for this Sequence")
            if common_difference >= 0:
                st.latex(f"a_n = {first_term} + (n-1) \\times {common_difference}")
            else:
                st.latex(f"a_n = {first_term} + (n-1) \\times ({common_difference})")
            
        except Exception as e:
            st.error(f"An error occurred while generating the sequence: {str(e)}")
    
    # Add some example usage
    with st.expander("ℹ️ Examples and Tips"):
        st.markdown("""
        **Examples:**
        - **Natural Numbers:** First term = 1, Common difference = 1
        - **Even Numbers:** First term = 2, Common difference = 2
        - **Decreasing Sequence:** First term = 10, Common difference = -1
        - **Decimal Sequence:** First term = 0.5, Common difference = 0.5
        
        **Tips:**
        - Use positive common difference for increasing sequences
        - Use negative common difference for decreasing sequences
        - Decimal values are supported for both terms and differences
        - Maximum of 1000 terms can be generated at once
        """)

if __name__ == "__main__":
    main()
